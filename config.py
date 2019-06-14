from easydict import EasyDict as edict
import os

cfg = edict()

cfg.github = edict()

# 基础配置，只需要配置这里
cfg.github.user_name = 'Hzzone'
cfg.github.repo_name = 'hzzone.github.io'
cfg.github.branch_name = 'source'

# github 开发者设置
cfg.github.base_url = 'https://api.github.com/repos/{}/{}'.format(cfg.github.user_name, cfg.github.repo_name)
cfg.github.source_branch_url = '{}/branches/{}'.format(cfg.github.base_url, cfg.github.branch_name)
cfg.github.commits_url = '{}/git/commits'.format(cfg.github.base_url)
cfg.github.file_commit_url = '{}/commits'.format(cfg.github.base_url)
cfg.github.tree_url = '{}/git/trees'.format(cfg.github.base_url)
cfg.github.blob_url = '{}/git/blobs'.format(cfg.github.base_url)



# notebook 预览地址
cfg.github.notebook_preview_url = 'https://nbviewer.jupyter.org/github/{}/{}/blob/{}'.format(
    cfg.github.user_name,
    cfg.github.repo_name,
    cfg.github.branch_name
)

# 本地读取的目录和生成目录
cfg.local = edict()
if 'GITHUB_TOKEN' in os.environ.keys():
    # travis 部署
    cfg.local.source = 'source'
    cfg.local.generate = 'generate'
else:
    # 本地
    cfg.local.source = '/Users/hzzone/Desktop/hzzone.github.io'
    cfg.local.generate = '/usr/local/Cellar/nginx/1.15.9/html'

# 个人设置：介绍，头像，名字
cfg.self = edict()
cfg.self.avatar = 'https://avatars2.githubusercontent.com/u/19267349'
cfg.self.short_introduction = 'To be talented & positive.'
cfg.self.name = 'Zhizhong Huang'

cfg.conversion = edict()
# 转换的后缀名，notebook 转成 md 再转 html
cfg.conversion.postfix = ['.md', '.ipynb']