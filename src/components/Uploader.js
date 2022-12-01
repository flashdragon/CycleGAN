import {useEffect, useState} from 'react';
import "./uploader.scss";
import {Button} from "@mui/material";
import axios from 'axios';

const Uploader = () => {

  const [image, setImage] = useState({
    image_file: "",
    preview_URL: require('./123.png'),
  });

  const [image2, setImage2] = useState(require('./123.png'));
  


  let inputRef;

  const saveImage = (e) => {
    e.preventDefault();
    if(e.target.files[0]){
      // 새로운 이미지를 올리면 createObjectURL()을 통해 생성한 기존 URL을 폐기
      URL.revokeObjectURL(image.preview_URL);
      const preview_URL = URL.createObjectURL(e.target.files[0]);
      setImage(() => (
        {
          image_file: e.target.files[0],
          preview_URL: preview_URL
        }
      ))
    }
  }

  const deleteImage = () => {
    // createObjectURL()을 통해 생성한 기존 URL을 폐기
    URL.revokeObjectURL(image.preview_URL);
    setImage({
      image_file: "",
      preview_URL: require('./123.png'),
    });
    setImage2(require('./123.png'));
  }

  useEffect(()=> {
    // 컴포넌트가 언마운트되면 createObjectURL()을 통해 생성한 기존 URL을 폐기
    return () => {
      URL.revokeObjectURL(image.preview_URL)
    }
  }, [])

  const sendImageToServer = async () => {
    if (image.image_file) {
      const formData = new FormData();
      formData.append('file', image.image_file);
      await axios({
        method:"post",
        url:'http://localhost:5000/',
        data:formData,
        responseType:"blob"
      })
      .then((res) => {
        const url = window.URL.createObjectURL(new Blob([res.data] ));
        console.log(res);
        setImage2(url);
    });
      alert("서버에 등록이 완료되었습니다!");
    } else {
      alert("사진을 등록하세요!")
    }
  }

  return (
    <div className="uploader-wrapper">
      <input type="file" accept="image/*"
             onChange={saveImage}
        // 클릭할 때 마다 file input의 value를 초기화 하지 않으면 버그가 발생할 수 있다
        // 사진 등록을 두개 띄우고 첫번째에 사진을 올리고 지우고 두번째에 같은 사진을 올리면 그 값이 남아있음!
             onClick={(e) => e.target.value = null}
             ref={refParam => inputRef = refParam}
             style={{display: "none"}}
      />
      <div className="img-wrapper">
        <div className='img-one'>
        <img src={image.preview_URL} />
        <p className='ttext'>이미지를 드래그 해주세요!</p>
        </div>
        <div className='img-one'>
        <img src={image2}/>
        <p className='ttext'>출력 이미지</p>
        </div>
      </div>

      <div className="upload-button">
        <Button type="primary" variant="contained" onClick={() => inputRef.click()}>
          Preview
        </Button>
        <Button color="error" variant="contained" onClick={deleteImage}>
          Delete
        </Button>
        <Button color="success" variant="contained" onClick={sendImageToServer}>
          Upload
        </Button>
      </div>
    </div>
  );
}

export default Uploader;