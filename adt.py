# The Redmi Note 10 Pro's device tree values, for build/mapple/tools/mkadt.py (with tools/soc/sm7150.py). From ios-sweet's
# tools/mkadt.py --highmem (damjankakak3); MIT.

# The whole upper DDR bank (live FDT memory <0x1_00000000 0xfcc00000>); every fixed reserved-memory carve-out is in the
# low bank and the dynamic pools are limited below 4G: (base, size).
RAM = (0x100000000, 0xfcc00000)
# ABL's splash framebuffer, sweet's panel (1080x2400).
FB = dict(base=0x9c000000, size=0x1700000, width=1080, height=2400, stride=1080 * 4)
ECID = 0x5357454554000001  # 'SWEET' + 1, synthetic
PRODUCT_NAME = 'Redmi Note 10 Pro'
DISPLAY_GAMUT = 'P3'    # as ios-sweet: the iPhone X's
# About: the global model, ro.product.odm.model=M2101K6G in LineageOS android_device_xiaomi_sweet (lineage-24.0, 894ae0b)
# properties/build_GLOBAL.prop (India: M2101K6P and M2101K6I, Japan: M2101K6R). serial-number is a placeholder the
# shim overwrites at each boot with ABL's androidboot.serialno.
ABOUT = dict(serial='MAPPLE0000000000', model='M2101K6G', region='', regulatory='M2101K6G')


def devices(a, ph, phandle, gic_ph, ecid, flags):
    """/arm-io devices: none; the kernel line's drivers find theirs by address."""
    return []
