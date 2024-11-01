// 생성자 함수 정의
function Samhundred() {
  // 1. schoolName이라는 키를 정적으로 추가합니다.
  this.schoolName = 'High School';

  // 2. schoolStudent라는 배열을 동적으로 추가합니다.
  this.schoolStudent = ['StudentA', 'StudentB', 'StudentC'];

  // 3. smile이라는 메서드를 동적으로 추가하여 schoolStudent 배열의 첫 번째 값을 출력합니다.
  this.smile = function() {
      console.log(this.schoolStudent[0]);
  };
}

// 생성자 함수를 사용하여 samhundred 객체를 생성합니다.
const samhundred = new Samhundred();

// 메서드 호출하여 확인
samhundred.smile(); // 출력: StudentA
