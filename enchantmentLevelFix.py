import json

# WIP

json.dump({f'enchantment.level.{i}': f'{i}' for i in range(11, 2147483648)}, open("enchlevelfixS.json", 'w', encoding='utf8'),
          indent=4, ensure_ascii=False)
