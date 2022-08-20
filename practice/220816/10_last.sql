-- AC/DC의 모든 앨범
-- AC/DC (artists)
-- 앨범(album)

-- 앨범 검색하려고 했는데
-- 아티스트는 id로 저장되어 있네요
-- AC/DC는 아는데 ID를 모르네요?

-- ID 조회
SELECT ArtistId
FROM artists
WHERE Name = 'Nirvana';
-- ArtistId
-- --------
-- 110

-- 서브쿼리
SELECT *
FROM albums
WHERE ArtistId = (SELECT ArtistId
FROM artists
WHERE Name = 'Nirvana');
-- AlbumId  Title
--                 ArtistId
-- -------  ----------------------------
-- --------------  --------
-- 163      From The Muddy Banks Of The 
-- Wishkah [Live]  110
-- 164      Nevermind
--                 110