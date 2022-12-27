<!doctype html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <title>Hello Mermaid</title>
 <meta name="description" content="A cool example of using
 mermaid">
 <meta name="author" content="Your Name">
 <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/
 mermaid.min.js"></script>
</head>
<body>
 <h1>Example</h1>
 <div class="mermaid">
    flowchart TB
    apple --> bear
 </div>

<script>
 var theCallbackFun = function(){
 alert('This callback was triggered!');
 }
 mermaid.initialize({
 theme: 'base',
 securityLevel: 'loose',
 });
 </script>
</body>
</html>
