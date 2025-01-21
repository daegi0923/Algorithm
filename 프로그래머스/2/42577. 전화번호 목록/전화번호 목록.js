function solution(phone_book) {
    const phoneMap = new Map();

    // 모든 전화번호를 해시맵에 저장
    for (const phone of phone_book) {
        phoneMap.set(phone, true);
    }

    // 각 전화번호의 접두어가 해시맵에 있는지 확인
    for (const phone of phone_book) {
        for (let i = 1; i < phone.length; i++) {
            const prefix = phone.slice(0, i);
            if (phoneMap.has(prefix)) {
                return false;
            }
        }
    }

    return true;
}
