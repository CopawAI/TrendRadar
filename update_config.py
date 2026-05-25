#!/usr/bin/env python3
import yaml

# 读取配置
with open('config/config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 启用钉钉推送
config['notification']['channels']['dingtalk']['webhook_url'] = 'DINGTALK_WEBHOOK_URL'  # 使用 GitHub Secret
config['notification']['channels']['dingtalk']['secret_key'] = 'DINGTALK_SECRET_KEY'  # 使用 GitHub Secret

# 选择监控平台（6个）
platform_ids = ['toutiao', 'baidu', 'wallstreetcn-hot', 'cls-hot', 'zhihu', 'weibo', 'douyin', 'bilibili-hot-search']
config['platforms']['sources'] = [s for s in config['platforms']['sources'] if s['id'] in platform_ids]

# 关闭 RSS（简化配置）
config['rss']['enabled'] = False

# 关闭 AI 分析（先用基础版测试）
config['ai_analysis']['enabled'] = False
config['ai_translation']['enabled'] = False

# 关闭 schedule，用固定时间推送
config['schedule']['enabled'] = False

# 保存配置
with open('config/config.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print('配置已更新')
print(f'启用的平台: {[s["id"] for s in config["platforms"]["sources"]]}')