const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', (line) => {
    input.push(line);
}).on('close', () => {
    const N = parseInt(input[0], 10);
    const arr = input[1].split(' ').map(Number);
    solution(N, arr);
});

function solution(N, arr) {
    let snackIn = 1;   // 올바른 순서로 쌓을 수 있는지 확인하는 기준
    let waitMiddle = []; // 중간에 쌓아두는 대기열

    for (let i = 0; i < N; i++) {
        const current = arr[i];
        
        // 현재 사람이 snackIn 순서와 같으면 바로 snackIn으로 쌓기
        if (current === snackIn) {
            snackIn++;
        } else {
            // 순서가 다르면 중간 대기열에 추가
            waitMiddle.push(current);
        }

        // 대기열에 쌓인 순서가 맞으면 snackIn으로 추가
        while (waitMiddle.length > 0 && waitMiddle[waitMiddle.length - 1] === snackIn) {
            waitMiddle.pop();
            snackIn++;
        }
    }

    // 최종적으로 snackIn이 N + 1에 도달했다면 모든 스낵을 순서대로 쌓을 수 있는 상태
    if (snackIn === N + 1) {
        console.log('Nice');
    } else {
        console.log('Sad');
    }
}