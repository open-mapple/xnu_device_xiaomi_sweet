# xnu_device_xiaomi_sweet

The Xiaomi Redmi Note 10 Pro (`sweet`: Qualcomm SM7150 (Snapdragon 732G), 1080x2400) for Open Mapple: its configuration (`device.conf`, `configs/`).
Board facts (touch chip, pins, buses, panel) live here, not in the kernel.

**Build-only.** Nobody on the project owns this phone, so the kernel has been built for it but never run. Upstream's reports
are in the credited projects; a maintainer with the phone is welcome (see NOTICE for whose work this builds on).

Status of the tip kernel on this phone: not run by us. Untested on sweet: the framebuffer present path (the kernel's
framebuffer code was extended for sunfish's panel and scaling; the default path shares the same functions), and the
IO submap sizing (its startup code changed; the default is still 8 MiB).

Untested here: the GPU user interface (`sweetgpuabi=1`, an msm-style IOKit client over the Adreno 618 service: it compiles and links, nothing opens it yet), and the GPU page-table mode (`sweetgpuvm=1`: a 1 GiB window of scattered pages and 2,048 buffers instead of the contiguous 64 MiB one; compiles, never run).

Boot-args and ADT flags are in `device.conf`. The kernel is built from `xnu_kernel_qcom_common` with `config/MASTER.arm64.sweet`.

Licence: MIT (`LICENSE`); `NOTICE` credits the upstream authors; `LEGAL.md` says what never goes in.
