// *************************************************
const root = document.getElementById('root');

const button = document.createElement('button');
button.textContent = "클릭";

const input = document.createElement("input");
input.placeholder = "아무거나";
input.name="test";

const clickForm = document.createElement('form');
clickForm.method= "POST";
clickForm.action="/click";
clickForm.appendChild(button);
clickForm.appendChild(input);


root.appendChild(clickForm);

// * <form method = "POST" action="/click">
  // * <button> 클릭합시다. </button>
// * <form>
// *************************************************

// window.navigator.serviceWorker.register()

// self.addEventListener("install", (event) => {
//   console.log(event);
//   event.waitUntil(
//     caches.open('app-cache')
//       .then((cache) => {
//         return cache.addAll(['./index.html']); // index.html을 캐싱합니다.
//       })
//   )
// });

// self.addEventListener('fetch', (event) => {
//   event.respondWith(
//     caches.match(event.request) // 요청과 일치하는 캐시를 찾습니다.
//       .then((response) => {
//         if (response) {
//           return response; // 캐시된 응답을 반환합니다.
//         }
//         return fetch(event.request); // 캐시가 없으면 네트워크 요청을 합니다.
//       })
//   );
// });