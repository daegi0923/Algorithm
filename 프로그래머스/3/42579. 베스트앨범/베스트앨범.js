function solution(genres, plays) {
    const genreCount = {}
    const genreSongs = {}
    
    // 1. 데이터 수집
    for(let i = 0; i < genres.length; i++){
        const genre = genres[i]
        const songCount = plays[i]
        if(!genreCount[genre]){
            genreCount[genre] = 0
            genreSongs[genre] = []
        }
        genreCount[genre] = genreCount[genre] + songCount
        genreSongs[genre].push({id : i, "play":songCount})

    }
    // console.log(genreCount)    
    // console.log(genreSongs)
    // 2. 장르별 재생횟수 정렬
    const sortedGenre = Object.keys(genreCount).sort((a, b) => genreCount[b] - genreCount[a])
    // console.log(sortedGenre)
    
    
    // 3. 장르별 많이 재생된 곡 추출
    const result = []
    sortedGenre.forEach(genre=>{
        const songList = genreSongs[genre]
        songList.sort((a, b) => b.play - a.play)
        // console.log(songList)
        result.push(songList[0].id)
        if(songList.length>=2){
            result.push(songList[1].id)
        }
    })
    return result
}