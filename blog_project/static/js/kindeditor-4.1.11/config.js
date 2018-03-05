 KindEditor.ready(function(K) {
                window.editor = K.create('textarea[name=content]',{
                    with:1000,
                    height:400,
                    uploadJson:'/admin/upload/kindeditor',
                });
        });