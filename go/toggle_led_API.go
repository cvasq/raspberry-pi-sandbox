// Starts an API service on port 3000 for toggling an LED light
// Toggle via CLI: curl localhost:3000/api/commands/led_toggle
package main

import (
	"gobot.io/x/gobot"
	"gobot.io/x/gobot/api"
	"gobot.io/x/gobot/drivers/gpio"
	"gobot.io/x/gobot/platforms/raspi"
)

func main() {

	gpioPin = "11"

	rpi := raspi.NewAdaptor()
	led := gpio.NewLedDriver(rpi, gpioPin)
	// Turn off LED on exit
	defer led.Off()

	master := gobot.NewMaster()

	a := api.NewAPI(master)
	a.Debug()
	a.Start()

	// Create the /api/commands/led_toggle endpoint
	master.AddCommand("led_toggle",
		func(params map[string]interface{}) interface{} {
			led.Toggle()
			return "Toggling LED!"
		})

	master.Start()
}
