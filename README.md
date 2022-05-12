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

# Author
特徴量選択、学習過程は下記のレポジトリ!!
(もはやこちらがメイン…)
