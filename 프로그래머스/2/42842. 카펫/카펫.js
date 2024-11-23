function solution(brown, yellow) {
    // 1. 가능한 height와 width 찾기
    for (let height = 1; height <= Math.sqrt(yellow); height++) {
        if (yellow % height !== 0) continue; // yellow의 약수인지 확인

        const width = yellow / height;

        // 2. 테두리에 필요한 brown 개수 계산
        const totalRequireBrown = (height + 2) * 2 + width * 2;
        if (totalRequireBrown === brown) {
            // 3. width >= height 순서를 보장
            return [Math.max(width, height) + 2, Math.min(width, height) + 2];
        }
    }
    return [];
}