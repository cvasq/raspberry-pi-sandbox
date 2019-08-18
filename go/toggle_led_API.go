package main

import (
	"gobot.io/x/gobot"
	"gobot.io/x/gobot/api"
	"gobot.io/x/gobot/drivers/gpio"
	"gobot.io/x/gobot/platforms/raspi"
)

func main() {

	rpi := raspi.NewAdaptor()
	led := gpio.NewLedDriver(rpi, "11")

	master := gobot.NewMaster()

	a := api.NewAPI(master)
	a.Debug()
	a.Start()

	// curl localhost:3000/api/commands/led_toggle
	master.AddCommand("led_toggle",
		func(params map[string]interface{}) interface{} {
			led.Toggle()
			return "Toggling LED!"
		})

	master.Start()

}
