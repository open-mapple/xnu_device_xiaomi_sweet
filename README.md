# xnu_device_xiaomi_sweet

The Xiaomi Redmi Note 10 Pro (`sweet`: Qualcomm SM7150 (Snapdragon 732G), 1080x2400) for Open Mapple: its configuration (`device.conf`, `configs/`).
Board facts (touch chip, pins, buses, panel) live here, not in the kernel.

**Build-only.** Nobody on the project owns this phone, so the kernel has been built for it but never run. Upstream's reports
are in the credited projects; a maintainer with the phone is welcome (see NOTICE for whose work this builds on).

Status of the tip kernel on this phone: not run by us. Untested on sweet: the framebuffer present path (the kernel's
framebuffer code was extended for sunfish's panel and scaling; the default path shares the same functions), and the
IO submap sizing (its startup code changed; the default is still 8 MiB).

Boot-args and ADT flags are in `device.conf`. The kernel is built from `xnu_kernel_qcom_common` with `config/MASTER.arm64.sweet`.

Licence: MIT (`LICENSE`); `NOTICE` credits the upstream authors; `LEGAL.md` says what never goes in.
