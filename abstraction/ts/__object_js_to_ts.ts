class Samhundred {
  schoolName: string;
  schoolStudent: string[];

  constructor(name: string, students: string[]) {
    this.schoolName = name;
    this.schoolStudent = students;
  }

  smile(): void {
    console.log(this.schoolStudent[0]);
  }
}

// Samhundred 객체를 각각 다른 데이터로 생성
const school1 = new Samhundred('High School A', ['Alice', 'Bob', 'Charlie']);
const school2 = new Samhundred('High School B', ['David', 'Emma', 'Frank']);

// 각 객체의 메서드를 호출
school1.smile(); // 출력: Alice
school2.smile(); // 출력: David