import re
from keyword import kwlist
from pathlib import Path

from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper

from steam.enums import common as common_enums
from tools.protobuf import protobufs_dir, source_code_dir

kwlist = set(kwlist + ['None'])

_proto_modules = ['enums_pb2']

for file in protobufs_dir.rglob('*.proto'):
    file: Path
    with file.open('r', encoding='utf-8') as f:
        data = f.read()
    if 'import "enums.proto"' in data:
        _proto_modules.append(f'{file.stem}_pb2')

_proto_module = __import__('steam.protobufs', globals(), locals(), _proto_modules, 0)

classes = {}

for name in _proto_modules:
    proto = getattr(_proto_module, name)
    gvars = globals()

    for class_name, value in proto.__dict__.items():
        if not isinstance(value, EnumTypeWrapper) or hasattr(common_enums, class_name):
            continue

        attrs_starting_with_number = False
        attrs = {}

        for ikey, ivalue in value.items():
            ikey = re.sub(r'^(k_)?(%s_)?' % class_name, '', ikey)
            attrs[ikey] = ivalue

            if ikey[0:1].isdigit() or ikey in kwlist:
                attrs_starting_with_number = True

        classes[class_name] = attrs, attrs_starting_with_number

# write enums as python Enum
with (source_code_dir / 'enums' / 'proto.py').open('w', encoding='utf-8') as f:
    f.write('from steam.enums.base import SteamIntEnum\n\n')

    for class_name, (attrs, attrs_starting_with_number) in sorted(
        classes.items(), key=lambda x: x[0].lower()
    ):
        if attrs_starting_with_number:
            f.write(f'\n{class_name} = SteamIntEnum({class_name!r}, {{\n')
            for ikey, ivalue in attrs.items():
                f.write(f'    {ikey!r}: {ivalue!r},\n')
            f.write('    })\n')
        else:
            f.write(f'\nclass {class_name}(SteamIntEnum):\n')
            for ikey, ivalue in attrs.items():
                f.write(f'    {ikey} = {ivalue}\n')
        f.write('\n')

    f.write('\n__all__ = [\n')

    for class_name in sorted(classes, key=lambda x: x.lower()):
        f.write(f'    {class_name!r},\n')

    f.write(']\n')
