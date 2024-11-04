var Samhundred = /** @class */ (function () {
    function Samhundred(name, students) {
        this.schoolName = name;
        this.schoolStudent = students;
    }
    Samhundred.prototype.smile = function () {
        console.log(this.schoolStudent[0]);
    };
    return Samhundred;
}());
// Samhundred 객체를 각각 다른 데이터로 생성
var school1 = new Samhundred('High School A', ['Alice', 'Bob', 'Charlie']);
var school2 = new Samhundred('High School B', ['David', 'Emma', 'Frank']);
// 각 객체의 메서드를 호출
school1.smile(); // 출력: Alice
school2.smile(); // 출력: David
