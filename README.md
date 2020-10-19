# py-wireframe-renderer
Quasi-rendering engine written in Python.

## Who does what here?

- **blenderToJSON.py**: He is a Blender script that exports 3D objects from Blender as JSON files.
- **draw3D.py**: He takes the JSON file and makes a Turtle drawing from it. :warning: SLOW :warning:
- **test9.json**: Example file. It is a hex nut. Takes about 3 minutes to render for me.
- **3dobj.schema.json**: JSON Schema for the JSON export.

## Does this work?

![](https://github.com/PlanMan1717/py-wireframe-renderer/blob/main/Screenshot%202020-10-19%20103802.png?raw=true)

Yes.

## Coming Soon...

- blenderToJSON.py should be a Blender Add-On.
- Optimizations
- Removing unused preoperties from the JSON.
- More examples.

# License: *Creative Commons Attribution Share-Alike* (CC BY-SA)

[License Text](https://creativecommons.org/licenses/by-sa/4.0/)

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
- **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
