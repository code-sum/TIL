-- 0822 오후 실습 코드 예제

-- INNER JOIN
SELECT * 
FROM albums JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;

-- LEFT OUTER JOIN
SELECT * 
FROM albums LEFT JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;