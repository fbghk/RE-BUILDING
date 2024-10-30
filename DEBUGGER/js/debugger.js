const myName = "임유진";
function a() {
  b();
  function b() {
    c();
    function c() {
      d();
      function d() {
        console.log(myName);
      }
    }
  }
}
a();