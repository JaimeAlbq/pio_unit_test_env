Import("env")

print("Start pre build script")

def pre_build(source, target, env):
    print("Installing QEMU")
    env.Execute("python $PROJECT_PACKAGES_DIR/framework-espidf/tools/idf_tools.py install qemu-xtensa qemu-riscv32")

env.AddPreAction("buildprog", pre_build)

print("End pre build script")
