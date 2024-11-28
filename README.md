# aiwolf-nlp-common

人狼知能コンテスト（自然言語部門） のエージェント向けの共通パッケージです。  
ゲームサーバから送信されるJSON形式のデータをオブジェクトに変換するためのパッケージです。

```python
import json

from aiwolf_nlp_common.protocol import Packet

recv: str = """{"request":"INITIALIZE","info":{"statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[02]":"SEER"},"remainTalkMap":{},"remainWhisperMap":{},"day":0,"agent":"Agent[02]"},"setting":{"roleNumMap":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":0,"SEER":1,"VILLAGER":3,"WEREWOLF":1},"maxTalk":3,"maxTalkTurn":15,"maxWhisper":3,"maxWhisperTurn":15,"maxSkip":3,"isEnableNoAttack":true,"isVoteVisible":false,"isTalkOnFirstDay":true,"responseTimeout":90000,"actionTimeout":60000,"maxRevote":1,"maxAttackRevote":1}}"""
value: dict = json.loads(recv)
packet = Packet(value=value)

print(packet.request)
print(packet.info.agent)
```

```
INITIALIZE
Agent[02]
```

詳細については下記のプロトコルの説明やゲームサーバのソースコードを参考にしてください。  
[プロトコルの実装について](https://github.com/kano-lab/aiwolf-nlp-server/blob/main/doc/protocol.md)

## インストール方法

```
pip install aiwolf-nlp-common
```

> [!WARNING]
> `pip install aiwolf-nlp-common` に失敗する場合は、以下の手順を試してください。

```
pip install --upgrade pip
pip install --upgrade setuptools
pip install -i https://test.pypi.org/simple/ aiwolf-nlp-common
```