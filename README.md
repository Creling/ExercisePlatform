# ExercisePlatform
## API
### 1. `/api/upload`提交作业
**方法**  
POST  

**格式**  
JSON  

**参数**   
|字段|数据类型|说明|
|----|----|----|
| hwkID | string | 作业编号 |
| hwkContent | string | 作业内容 |

**响应**  
|字段|数据类型|说明|
|----|----|----|
| response | string | 作业批改结果 |

### 2. `/api/hwkid`获取支持的作业编号
**方法**  
GET  

**格式**  
JSON  

**响应**  
|字段|数据类型|说明|
|----|----|----|
| filename | list | 保存所有作业编号的一个list |
