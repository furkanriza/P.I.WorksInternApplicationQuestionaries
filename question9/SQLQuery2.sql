SELECT 
    Device_Type, 
    SUBSTRING(
        Stats_Access_Link, 
        CHARINDEX('://', Stats_Access_Link) + 3, 
		CHARINDEX('</', Stats_Access_Link, CHARINDEX('://', Stats_Access_Link) + 3) - CHARINDEX('://', Stats_Access_Link) - 3
    ) AS Pure_URL
FROM 
	Table_1