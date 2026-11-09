# NS11 full pass render: open the AOV variant blend and render it as built
# (scene carries the comp tree, EXR passes File Output, and PNG comp output).
import bpy, sys
def main():
    bpy.ops.render.render(write_still=True)
    print("OK ns11_full_render")
main()
