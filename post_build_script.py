Import("env")

print("Start post build script")

def after_build(source, target, env):
    print("Removing old result.bin")
    # env.Execute("rm $PROJECT_DIR/result.bin")
    print("Creating new result.bin")
    env.Execute("$PROJECT_PACKAGES_DIR/tool-esptoolpy/esptool.py --chip esp32 merge_bin --output result.bin --fill-flash-size 4MB 0x1000 $PROJECT_BUILD_DIR/lilygo-t-display/bootloader.bin 0x8000 $PROJECT_BUILD_DIR/lilygo-t-display/partitions.bin 0x10000 $PROJECT_BUILD_DIR/lilygo-t-display/firmware.bin --flash_mode dio --flash_freq 40m --flash_size 4MB")

env.AddPostAction("$BUILD_DIR/firmware.bin", after_build)

print("End post build script")
