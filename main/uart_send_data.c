#include "driver/gpio.h"
#include "driver/usb_serial_jtag.h"
#include "esp_err.h"
#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/projdefs.h"
#include "freertos/task.h"
#include "hal/gpio_types.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BUF_SIZE (1024)
#define LED_GPIO GPIO_NUM_6

static const char *TAG = "JTAG_SERIAL";

static int blink_hz = 0;
static int led_on = 0;

static void configure_gpio(void) {
    gpio_config_t gpio_conf = {
        .pin_bit_mask = (1ULL << LED_GPIO),
        .mode = GPIO_MODE_OUTPUT,
        .pull_up_en = GPIO_PULLUP_DISABLE,
        .pull_down_en = GPIO_PULLDOWN_DISABLE,
        .intr_type = GPIO_INTR_DISABLE,
    };
    gpio_config(&gpio_conf);
    gpio_set_level(LED_GPIO, 0);
}

static void parse_blink_cmd(char *buffer) {
    char mode[10];
    int freq;

    if (sscanf(buffer, "%[^,],%d", mode, &freq) == 2) {
        ESP_LOGI(TAG, "Parsed: mode=%s, freq=%d", mode, freq);
        blink_hz = freq;

        if (strcmp(mode, "ON") == 0) {
            ESP_LOGI(TAG, "LED ON");
            led_on = 1;
        } else if (strcmp(mode, "OFF") == 0) {
            ESP_LOGI(TAG, "LED OFf");
            led_on = 0;
        }
    } else {
        ESP_LOGW(TAG, "Parse error");
    }
}

static void usb_serial_task(void *arg) {
    uint8_t *data = (uint8_t *)malloc(BUF_SIZE);
    usb_serial_jtag_driver_config_t usb_serial_conf = {
        .rx_buffer_size = BUF_SIZE,
        .tx_buffer_size = BUF_SIZE,
    };

    ESP_ERROR_CHECK(usb_serial_jtag_driver_install(&usb_serial_conf));

    static char buffer[256];
    static int index = 0;
    while (1) {
        int len = usb_serial_jtag_read_bytes(data, BUF_SIZE - 1,
                                             100 / portTICK_PERIOD_MS);
        if (len > 0) {
            data[len] = '\0';
            for (int i = 0; i < len; i++) {
                char c = data[i];
                if (c == '\n') {
                    buffer[index] = '\0';
                    ESP_LOGI(TAG, "Complete message: %s", buffer);
                    parse_blink_cmd(buffer);
                    index = 0;
                } else if (index < sizeof(buffer) - 1) {
                    buffer[index++] = c;
                } else {
                    ESP_LOGW(TAG, "Buffer overflow - resetting");
                    index = 0;
                }
            }
        }
    }
    free(data);
}

static void blink_task(void *arg) {
    while (1) {
        if (blink_hz > 0 && led_on) {
            gpio_set_level(LED_GPIO, 1);
            vTaskDelay(pdMS_TO_TICKS(blink_hz));
            gpio_set_level(LED_GPIO, 0);
            vTaskDelay(pdMS_TO_TICKS(blink_hz));
        } else if (led_on) {
            gpio_set_level(LED_GPIO, 1);
            vTaskDelay(pdMS_TO_TICKS(100));
        } else {
            gpio_set_level(LED_GPIO, 0);
            vTaskDelay(pdMS_TO_TICKS(100));
        }
    }
}

void app_main(void) {
    ESP_LOGI(TAG, "Configuring GPIO");
    configure_gpio();
    ESP_LOGI(TAG, "Initializing JTAG, waiting for data");
    xTaskCreate(usb_serial_task, "usb_serial_task", 4096, NULL, 5, NULL);
    xTaskCreate(blink_task, "blink_task", 4096, NULL, 5, NULL);
}
