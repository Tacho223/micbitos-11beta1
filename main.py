input.onButtonPressed(Button.A, function () {
    Knopf_A = 1
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    enter = 1
    if (file_number > 0) {
        App_use = 1
    }
    if (App_use == 1) {
        file_number = 0
    }
})
input.onButtonPressed(Button.B, function () {
    Knopf_B = 1
})
let satndby_mode = 0
let Light_blue = 0
let Pink = 0
let yellow = 0
let blue = 0
let green = 0
let red = 0
let white = 0
let vga_b = 0
let vga_g = 0
let vga_r = 0
let VSYNC = 0
let HSYNC = 0
let Zugewiesene_nummer = 0
let Max_file_number = 0
let temp_data = 0
let komp_data = 0
let light_data = 0
let PS2_output_enable = 0
let PS2_clck_data_1 = 0
let PS2_result = ""
let PS2_data = ""
let PS2_buffer_1 = 0
let Knopf_B = 0
let App_use = 0
let file_number = 0
let enter = 0
let Knopf_A = 0
let grey = 0
let black = 0
let pixel_trigger = 0
let OS_start = 1
music.playMelody("A E F - B A F G ", 300)
for (let index = 0; index < 49; index++) {
    pixel_trigger = 1
    black = 1
}
for (let index = 0; index < 17; index++) {
    pixel_trigger = 1
    grey = 1
}
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P15) == 1) {
        if (PS2_buffer_1 == 0) {
            PS2_buffer_1 = 1
        }
        if (PS2_buffer_1 == 1) {
            if (pins.digitalReadPin(DigitalPin.P15) == 1) {
                PS2_data = "" + PS2_data + pins.digitalReadPin(DigitalPin.P14)
            }
            if (PS2_data.length == 8) {
                PS2_result = PS2_data
                if (pins.digitalReadPin(DigitalPin.P15) == 1) {
                    PS2_clck_data_1 = PS2_clck_data_1 + 1
                    if (PS2_clck_data_1 == 2) {
                        PS2_clck_data_1 = 0
                        PS2_output_enable = 0
                        PS2_buffer_1 = 0
                        PS2_data = ""
                        PS2_result = ""
                    }
                }
            }
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
        if (PS2_result == "") {
        	
        }
    }
})
basic.forever(function () {
    light_data = input.lightLevel()
    komp_data = input.compassHeading()
    temp_data = input.temperature()
    serial.redirect(
    SerialPin.USB_TX,
    SerialPin.USB_RX,
    BaudRate.BaudRate115200
    )
    if (OS_start == 1) {
        if (!(App_use == 1)) {
            if (Knopf_A == 1) {
                file_number = file_number - 1
                Knopf_A = 0
            }
            if (Knopf_B == 1) {
                file_number = file_number + 1
                Knopf_B = 0
            }
            if (file_number == 0) {
                file_number = 1
            }
            if (file_number == Max_file_number + 1) {
                Max_file_number = Max_file_number
            }
            if (Max_file_number == Max_file_number + 1) {
                Zugewiesene_nummer = Zugewiesene_nummer + 1
            }
        }
    }
    if (HSYNC == 40) {
        VSYNC = VSYNC + 1
        pins.digitalWritePin(DigitalPin.P12, 1)
        pins.digitalWritePin(DigitalPin.P12, 0)
    }
    if (VSYNC == 30) {
        VSYNC = 0
        HSYNC = 0
    }
    if (vga_r > 255) {
        vga_r = 255
    }
    if (vga_g > 255) {
        vga_g = 255
    }
    if (vga_b > 255) {
        vga_b = 255
    }
    if (pixel_trigger == 1) {
        pins.digitalWritePin(DigitalPin.P16, 1)
        pins.digitalWritePin(DigitalPin.P16, 0)
        pixel_trigger = 0
        pixel_trigger = 0
        HSYNC = HSYNC + 1
        pins.analogWritePin(AnalogPin.P0, vga_r)
        pins.analogWritePin(AnalogPin.P1, vga_g)
        pins.analogWritePin(AnalogPin.P2, vga_b)
        if (white == 1) {
            pins.analogWritePin(AnalogPin.P0, 239)
            pins.analogWritePin(AnalogPin.P1, 238)
            pins.analogWritePin(AnalogPin.P2, 228)
            white = 0
        }
        if (black == 1) {
            pins.analogWritePin(AnalogPin.P0, 63)
            pins.analogWritePin(AnalogPin.P1, 41)
            pins.analogWritePin(AnalogPin.P2, 56)
            black = 0
        }
        if (grey == 1) {
            pins.analogWritePin(AnalogPin.P0, 141)
            pins.analogWritePin(AnalogPin.P1, 139)
            pins.analogWritePin(AnalogPin.P2, 145)
            grey = 0
        }
        if (red == 1) {
            pins.analogWritePin(AnalogPin.P0, 255)
            pins.analogWritePin(AnalogPin.P0, 0)
            pins.analogWritePin(AnalogPin.P0, 0)
            red = 0
        }
        if (green == 1) {
            pins.analogWritePin(AnalogPin.P0, 0)
            pins.analogWritePin(AnalogPin.P1, 216)
            pins.analogWritePin(AnalogPin.P2, 0)
            green = 0
        }
        if (blue == 1) {
            pins.analogWritePin(AnalogPin.P0, 0)
            pins.analogWritePin(AnalogPin.P1, 0)
            pins.analogWritePin(AnalogPin.P2, 255)
            blue = 0
        }
        if (yellow == 1) {
            pins.analogWritePin(AnalogPin.P0, 255)
            pins.analogWritePin(AnalogPin.P1, 255)
            pins.analogWritePin(AnalogPin.P2, 0)
            yellow = 0
        }
        if (Pink == 1) {
            pins.analogWritePin(AnalogPin.P0, 1023)
            pins.analogWritePin(AnalogPin.P0, 1023)
            pins.analogWritePin(AnalogPin.P0, 1023)
            Pink = 0
        }
        if (Light_blue == 1) {
            pins.analogWritePin(AnalogPin.P0, 0)
            pins.analogWritePin(AnalogPin.P1, 149)
            pins.analogWritePin(AnalogPin.P2, 255)
            Light_blue = 0
        }
    }
})
loops.everyInterval(3000, function () {
    if (EventBusValue.MICROBIT_EVT_ANY == 0) {
        satndby_mode = 1
    }
    if (EventBusSource.MICROBIT_ID_BUTTON_A == 1) {
        satndby_mode = 0
    }
})
loops.everyInterval(0.5, function () {
    let Picture_Enable = 0
    if (Picture_Enable == 1) {
        pixel_trigger = 1
    }
})
