# 2値分類タスクにおける自作モデルをAPI化したものです。
https://lightgbm-api.herokuapp.com/

テーマ: Spaceship Titanic!
<物語の概要>
宇宙の謎を解くためにデータサイエンスのスキルが必要な2912年へようこそ。4光年離れた場所から送信を受信しましたが、状況は良くありません。
宇宙船タイタニック号は、1か月前に打ち上げられた星間客船でした。約13,000人の乗客を乗せたこの船は、太陽系から近くの星を周回する3つの新しく居住可能な太陽系外惑星に移民を輸送する航海に出発しました。最初の目的地であるかに座55番星に向かう途中でアルファケンタウリを丸めている間、不注意な宇宙船タイタニックは、塵の雲の中に隠された時空の異常と衝突しました。悲しいことに、それは1000年前の同名の人と同じような運命をたどりました。船は無傷のままでしたが、乗客のほぼ半数が別の次元に輸送されました！
乗組員を救助し、失われた乗客を回収するために、宇宙船の損傷したコンピューターシステムから復元された記録を使用して、異常によってどの乗客が輸送されたかを予測することが求められます。
* テーマはkaggleにて https://www.kaggle.com/competitions/spaceship-titanic/overview

## 主に使用したライブラリ
* lightgbm
* Flask 
* heroku(デプロイ先)

## このAPIの実行サンプルはこちら
- https://github.com/takayanagishinnosuke/LightGBM_API_Test/blob/main/index.html
- 変数11個をjsonにてpostして、推論結果（true=1, false=0 をjsonで返す)

```bash
   let JSONdata = {
          A: $("#A").val(),
          B: $("#B").val(),
          C: $("#C").val(),
          D: $("#D").val(),
          E: $("#E").val(),
          F: $("#F").val(),
          G: $("#G").val(),
          H: $("#H").val(),
          I: $("#I").val(),
          J: $("#J").val(),
          K: $("#K").val(),
        };
```
```bash
      $.ajax({
          type : "POST",
          url : "https://lightgbm-api.herokuapp.com/",
          data : JSON.stringify(JSONdata),
          contentType: 'application/JSON',
          dataType : 'json',
          scriptCharset: 'utf-8',
          success : function(data) {
              // Success
              alert("success!");
              alert(JSON.stringify(data));
              $("#response").html(JSON.stringify(data));
          },
          error : function(data) {
              // Error
              alert("error");
              alert(JSON.stringify(data));
              $("#response").html(JSON.stringify(data));
          }
```

# 学習過程
https://github.com/takayanagishinnosuke/kaggle_SpacesShip/blob/main/kagle.py
* 特徴量選択、学習過程は上記のレポジトリにて解説(こちらがメインともいえる…)
* モデル定義~.pkl保存前コードのみ抜粋

```bash
"""LightGBMで学習"""
"""まずは必要なライブラリをimport"""
from sklearn.model_selection import train_test_split
from sklearn import metrics
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold

"""学習用と検証用でsplitする"""
X_data_train, X_data_valid, y_data_train, y_data_valid = train_test_split(
  x_data, y_data, test_size=0.3, random_state=0, stratify=y_data)

# X_data_train.head() #学習用の説明変数
# X_data_valid.head() #検証用の説明変数
# y_data_train.head() #学習用の目的変数
# y_data_valid.head() #検証用の目的変数

"""モデル作成"""
#モデル用にデータを格納する
lgb_data_train = lgb.Dataset(X_data_train,y_data_train)
lgb_data_eval = lgb.Dataset(X_data_valid,y_data_valid, reference=lgb_data_train)

"""パラメータの設定"""
params = {
  'objective': 'binary' ##目的変数は二値分類だよと設定
}

"""ハイパーパラメータの設定"""
model4 = lgb.train(params, lgb_data_train, valid_sets=lgb_data_eval,verbose_eval=10,num_boost_round=1000,early_stopping_rounds=10)
#(パラメータ, 学習データ, valid_sets=検証データ, verbose_eval=10回の学習毎に画面に表示するよ, num_boost_round=勾配Boostingを何回, early_stopping_rounds=過学習を防ぐために様子見何回するか)

"""予測してみる"""
y_data_pred = model4.predict(test_data2, num_iteration=model4.best_iteration)
#(予測データ, num_iteration=作成モデル名.best_iteration(ベストな探索回数で予測してね))

y_data_pred

"""0.5以上で1と予測したとみなす"""
y_data_pred = (y_data_pred > 0.5).astype(int)
y_data_pred[:5]

"""訓練データと検証データの正解率を確認"""
print(metrics.accuracy_score(y_data_train['Transported'],np.round(model4.predict(X_data_train))))
#1:訓練データの正解率は0.8036

print(metrics.accuracy_score(y_data_valid['Transported'],np.round(model4.predict(X_data_valid))))
#1:検証データ正解率は0.7553

"""pickleで保存しておく"""
import pickle

with open('lgbm_model.pkl', mode='wb') as f:
   pickle.dump(model4, f)

```
