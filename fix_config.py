import yaml

# 读取YAML文件
with open('new.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

proxies = data['proxies']

proxy_dict = {}

for proxy in proxies:
    proxy_dict[proxy['name']] = proxy


data['proxies'] = list(proxy_dict.values())

with open('fixed.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file)