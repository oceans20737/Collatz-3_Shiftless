# **Shiftless Collatz-3 Model**  
Hiroshi Harada — May 2, 2026

## **概要**
本リポジトリは、3-adic（3進数体）における Collatz 写像から「右シフトによる情報消失」を排除した情報保存的モデルである
**Shiftless 3-adic Collatz (Collatz-3)** のシミュレーションおよび可視化を行う Pythonコード群です。

Shiftlessモデルは以下を可視化することを目的としています：

- **キャリー雪崩の幾何学構造**  
- **A項（純粋膨張）と B項（補数注入）の干渉モアレ**  
- **3-adic 特有のフラクタル構造（ガスケット）**

---

## **内容物**

### **ドキュメント**
- **TITLE_EN**  
  論文タイトルページ（英語版）
- **REPORT_JP / REPORT_EN**  
  本研究の理論的背景、Shiftless Collatz-3 の線形分解および各 Figureの詳細な解説をまとめた研究レポート。

---

## **ソースコード**
各スクリプトを実行すると、対応する Figure（PNG）が自動生成されます。

---

### **`code_01.py`**  
標準 3-adic Collatzモデルとの同値性を確認します。  
軌道の **非3倍数部分（u<sub>k</sub>）** を抽出し、標準モデルと一致することを示します。  
出力：`figure1.png`, `figure1.csv`

---

### **`code_02.py`**  
Shiftless Collatz-3 の **コンパクト軌道** を可視化します。  
NZT=2 による **強烈なキャリー雪崩** を抽出します。  
出力：`figure2.png`

---

### **`code_03.py`**  
Shiftless Collatz-3 の 1ステップを次の 2フェーズに分解して、**フル軌道** を描画します。  
- **Reach（3進表記での左シフト + 自己重ね合わせ）**  
- **Fill（NZT 注入による局所的歪み）**  

出力：`figure3.png`

---

### **`code_04.py`**  
3種のダイナミクスを時間同期で比較します：

- 純粋膨張： 4n
- 固定加算： 4n + 1
- Shiftless： 4n + c<sub>k</sub> * 3<sup>v<sub>k</sub></sup>

構造の違いを並置して可視化します。  
出力：`figure4.png`

---

### **`code_05.py`**  
軌道を次のように線形分解し、両者の **空間的干渉（モアレ）** を可視化します。  

- **A項（純粋膨張）**  
- **B項（補数干渉）**  

出力：`figure5.png`

---

## **動作環境**
- Python 3.x  
- NumPy  
- Matplotlib  

---

## **使用方法**
ターミナルまたはコマンドプロンプトで各スクリプトを実行してください。

```bash
python code_01.py
python code_02.py
python code_03.py
python code_04.py
python code_05.py
```

---

## **License**
- Research Document: CC BY 4.0  
- Python Source Code: MIT License  
- © 2026 Hiroshi Harada

---
