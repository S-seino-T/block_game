# block_game

## environment
- Mac OSのみサポート
  - arm64
- `uv` (https://docs.astral.sh/uv/)
- Python 3.11
- ライブラリは`requirements.txt`に記載

## How to Play
### コマンドで実行
```
uv init
uv add -r requirements.txt
uv run main.py
```

### 実行可能ファイルを生成
- 上記コマンドを実行
```
pyinstaller --onefile --noconsole main.py
```

- 実行後`dist`ディレクトリにファイルが生成される