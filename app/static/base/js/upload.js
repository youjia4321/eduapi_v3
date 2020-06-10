 function selectImg() {
    if(confirm("是否确定更改头像？")) {
        $("#upload").click()
    }
}

function upload(file) {
    if(file.type.startsWith('image/')) {
        if(!(file.size > 1024*1024*2)) {
            const myMsg = layer.msg('正在上传，请稍等...', {
                shade: 0.4,
                time: false //取消自动关闭
            });
            var formData = new FormData();
            formData.append("photo", file);
            $.ajax({
                url: '/user/upload',
                type: 'post',
                cache: false,    //上传文件不需要缓存
                dataType: 'json',
                data: formData,
                processData: false, // 告诉jQuery不要去处理发送的数据
                contentType: false, // 告诉jQuery不要去设置Content-Type请求头
                success: function (result) {
                    if(result.code === 200) {
                        layer.close(myMsg); //手动关闭
                        $("#photoImg").attr('src', result.path);
                    }
                }
            });
        } else {
            layer.msg('上传图片限制2M以内，请重试', {
                time: 2000,
                shade: 0.4,
                icon: 2
            })
        }
    } else {
        layer.msg('上传文件类型限制为图片，请重试', {
            time: 2000,
            shade: 0.4,
            icon: 2
        })
    }
}