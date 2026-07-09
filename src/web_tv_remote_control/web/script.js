function sendkey(action) {
  fetch('/key/' + action, { method: 'post' }).catch(e => console.log(e));
}

if ("serviceworker" in navigator) {
  navigator.serviceworker.register("/sw.js");
}
