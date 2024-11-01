// 1. samhundred라는 객체를 초기화합니다.
const samhundred = {};

// 2. schoolName이라는 키를 정적으로 추가합니다.
samhundred.schoolName = 'High School';

// 3. schoolStudent라는 배열을 동적으로 추가합니다.
samhundred.schoolStudent = ['StudentA', 'StudentB', 'StudentC'];

// 4. 임의의 키로 메서드를 동적으로 추가하고, 배열의 0번째 값을 출력하는 기능을 구현합니다.
samhundred.smile = function() {
    console.log(this.schoolStudent[0]);
};

// 메서드 호출하여 확인
samhundred.smile(); // 출력: StudentA