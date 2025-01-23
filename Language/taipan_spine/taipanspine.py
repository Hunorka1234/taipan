import os
import importlib
from pathlib import Path

class TaipanSpine:
    def __init__(self):
        self.modules = {}
        self.module_list = []
        self.load_all_modules()
        for name, module in self.modules.items():
            if hasattr(module, 'init_module'):
                setattr(self, name, module.init_module())
            else:
                setattr(self, name, module)

    def load_all_modules(self):
        modules_path = Path(__file__).parent.parent / 'taipan_tails' / 'modules'
        for file in modules_path.glob('*.py'):
            if file.name != '__init__.py':
                module_name = file.stem
                full_module_path = f"taipan_tails.modules.{module_name}"
                try:
                    module = importlib.import_module(full_module_path)
                    self.modules[module_name] = module
                    self.module_list.append(module_name)
                    print(f"Loaded module: {module_name}")
                except Exception as e:
                    print(f"Module loading info: {module_name} - {str(e)}")

    def get_function(self, func_name):
        for module in self.modules.values():
            if hasattr(module, 'init_module'):
                module_instance = module.init_module()
                if hasattr(module_instance, func_name):
                    return getattr(module_instance, func_name)
        return None

spine = TaipanSpine()
__all__ = ['spine'] + list(spine.modules.keys())
globals().update({name: getattr(spine, name) for name in spine.modules.keys()})
