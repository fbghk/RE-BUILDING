const fs = require('fs');
const path = require('path');

function readJsonFile(filePath) {
    // 파일 경로를 절대 경로로 변환
    const absolutePath = path.resolve(filePath);

    // 파일 존재 여부 확인
    fs.access(absolutePath, fs.constants.F_OK, (err) => {
        if (err) {
            console.log(`파일을 찾을 수 없습니다: ${absolutePath}`);
            return;
        }

        // 파일이 존재하면 읽기
        fs.readFile(absolutePath, 'utf8', (err, data) => {
            if (err) {
                console.error(`파일을 읽는 중 오류가 발생했습니다: ${err}`);
                return;
            }

            try {
                const jsonData = JSON.parse(data);
                console.log(jsonData);
            } catch (parseErr) {
                console.error(`JSON 파싱 오류가 발생했습니다: ${parseErr}`);
            }
        });
    });
}

// 사용 예시
const filePath = 'pitcher.json';
readJsonFile(filePath);