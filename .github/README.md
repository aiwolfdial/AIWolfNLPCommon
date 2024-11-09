# AIWolfNLP-Common

## 概要
人狼知能大会自然言語部門に参加する方向けのパッケージです。
aiwolf-nlp-serverから送信されるプロトコルからオブジェクトを作成し、返却します。

## 使い方

### サンプルコード
以下のコードでは、ゲームサーバから受け取ったJSON形式の文字列を使用してオブジェクトを生成します。生成されたオブジェクトは、JSONデータ内の値にアクセスできるように設計されており、Keyを指定することでデータを取り出すことができます。
例えば、以下のサンプルでは request や agent の情報にアクセスしています。

```python
from aiwolf_nlp_common.protocol import CommunicationProtocol

recv:str = """{"request":"INITIALIZE","info":{"statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[02]":"SEER"},"remainTalkMap":{},"remainWhisperMap":{},"day":0,"agent":"Agent[02]"},"setting":{"roleNumMap":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":0,"SEER":1,"VILLAGER":3,"WEREWOLF":1},"maxTalk":3,"maxTalkTurn":15,"maxWhisper":3,"maxWhisperTurn":15,"maxSkip":3,"isEnableNoAttack":true,"isVoteVisible":false,"isTalkOnFirstDay":true,"responseTimeout":90000,"actionTimeout":60000,"maxRevote":1,"maxAttackRevote":1}}"""
protocol = CommunicationProtocol.initialize_from_json(received_str=recv)

print(protocol.request)        # JSON内の "request" の値を取得
print(protocol.info.agent)     # JSON内の "info" の中の "agent" の値を取得
```

### 実行結果
```
INITIALIZE
Agent[02]
```

詳細については下記のプロトコルの説明やソースコードを参考にしてください。
> プロトコルについて： https://github.com/kano-lab/aiwolf-nlp-server/blob/main/doc/protocol.md

## 手順
```
$ pip install aiwolf-nlp-common
```

> [!WARNING]
> `pip install aiwolf-nlp-common` に失敗する場合は、以下のURLを参照してください。
> https://pypi.org/project/aiwolf-nlp-common/0.0.1/