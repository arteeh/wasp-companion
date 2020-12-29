## Wasp Companion

This is a Linux companion app for [wasp-os](https://github.com/daniel-thompson/wasp-os), a smartwatch operating system. It's written in Python with GTK and Libhandy.

This software is early in development so things are guaranteed to break.

### Functionality

On the front end, this app will:

- Show a graph of heartbeat data
- Show a graph of step counter data
- Add, update or remove apps
- Update wasp-os (DFU)
- Present settings (brightness, bluetooth, notifications, set a watchface, go to the bootloader, turn on the flashlight, restart the watch)

Behind the scenes, it will:

- Synchronize the time on the watch (RTC)
- Control music that's playing on your phone
- Sync the timer and stopwatch with the Clock app on your phone

### Building

You will need to have the following flatpaks installed:

- `org.gnome.Builder`
- `org.gnome.Sdk//3.38`

Enter the `flatpak` directory and run `./flatpak` for build commands. Run `./flatpak -f` to build everything.

When building is finished, you can run `./flatpak -p` to run the app. Be aware that building the app like this will not make it show up in your app list, and I'm not sure why.

### About me

I've been casually hanging around the PineTime community since about November 2019, talking to people in the chat. I've made [UI designs and mockups for a PineTime operating system](https://www.gitlab.com/arteeh/pinetimeos), and I've built [a GTK app in C in which you can flash the PineTime using an ST-Link](https://gitlab.com/arteeh/pinetime-flasher).

On Matrix I'm @arteeh:matrix.org and you can otherwise find me using the links on [my website](https://www.arteeh.com/).

### Credits

- [Daniel Thompson](https://github.com/daniel-thompson) for creating wasptool and its dependencies, which this app uses in the background.

### Useful links

- [Python GTK reference](https://lazka.github.io/pgi-docs/)
