<template>
  <div>
    <!-- picture-->
    <el-upload
      class="avatar-uploader"
      :action="getActionUrl"
      name="file"
      :headers="header"
      :show-file-list="false"
      :on-success="uploadSuccess"
      :on-error="uploadError"
      :before-upload="beforeUpload"
    ></el-upload>

    <quill-editor
      class="editor"
      v-model="value"
      ref="myQuillEditor"
      :options="editorOption"
      @blur="onEditorBlur($event)"
      @focus="onEditorFocus($event)"
      @change="onEditorChange($event)"
    ></quill-editor>
  </div>
</template>
<script>

const toolbarOptions = [
  ["bold", "italic", "underline", "strike"], 
  ["blockquote", "code-block"],
  [{ header: 1 }, { header: 2 }], // title
  [{ list: "ordered" }, { list: "bullet" }], 
  [{ script: "sub" }, { script: "super" }], 
  [{ indent: "-1" }, { indent: "+1" }],
  // [{'direction': 'rtl'}],                        
  [{ size: ["small", false, "large", "huge"] }], 
  [{ header: [1, 2, 3, 4, 5, 6, false] }], // title
  [{ color: [] }, { background: [] }], 
  [{ font: [] }], 
  [{ align: [] }], 
  ["clean"], 
  ["link", "image", "video"] 
];

import { quillEditor } from "vue-quill-editor";
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

export default {
  props: {
    value: {
      type: String
    },
    action: {
      type: String
    },
    maxSize: {
      type: Number,
      default: 4000 //kb
    }
  },

  components: {
    quillEditor
  },

  data() {
    return {
      content: this.value,
      quillUpdateImg: false, 
      editorOption: {
        placeholder: "",
        theme: "snow", // or 'bubble'
        modules: {
          toolbar: {
            container: toolbarOptions,
            // container: "#toolbar",
            handlers: {
              image: function(value) {
                if (value) {
                  document.querySelector(".avatar-uploader input").click();
                } else {
                  this.quill.format("image", false);
                }
              }
              // link: function(value) {
              //   if (value) {
              //     var href = prompt('url');
              //     this.quill.format("link", href);
              //   } else {
              //     this.quill.format("link", false);
              //   }
              // },
            }
          }
        }
      },
      // serverUrl: `${base.url}sys/storage/uploadSwiper?token=${storage.get('token')}`, // 这里写你要上传的picture服务器address
      header: {
        // token: sessionStorage.token
       'Token': this.$storage.get("Token")
      }
    };
  },
  computed: {
  
    getActionUrl: function() {
      // return this.$base.url + this.action + "?token=" + this.$storage.get("token");
      return `/${this.$base.name}/` + this.action;
    }
  },
  methods: {
    onEditorBlur() {
    },
    onEditorFocus() {
    },
    onEditorChange() {
      console.log(this.value);
      this.$emit("input", this.value);
    },
    beforeUpload() {
      this.quillUpdateImg = true;
    },

    uploadSuccess(res, file) {
      let quill = this.$refs.myQuillEditor.quill;
      if (res.code === 0) {
        let length = quill.getSelection().index;
        quill.insertEmbed(length, "image", this.$base.url+ "upload/" +res.file);
        quill.setSelection(length + 1);
      } else {
        this.$message.error("picture");
      }
      this.quillUpdateImg = false;
    },
    uploadError() {
      this.quillUpdateImg = false;
      this.$message.error("picture");
    }
  }
};
</script> 

<style>
.editor {
  line-height: normal !important;
}
.ql-snow .ql-tooltip[data-mode="link"]::before {
  content: "address:";
}
.ql-snow .ql-tooltip.ql-editing a.ql-action::after {
  border-right: 0px;
  content: "";
  padding-right: 0px;
}

.ql-snow .ql-tooltip[data-mode="video"]::before {
  content: "address:";
}
.ql-container {
	height: 400px;
}

.ql-snow .ql-picker.ql-size .ql-picker-label::before,
.ql-snow .ql-picker.ql-size .ql-picker-item::before {
  content: "14px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="small"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="small"]::before {
  content: "10px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="large"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="large"]::before {
  content: "18px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="huge"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="huge"]::before {
  content: "32px";
}

.ql-snow .ql-picker.ql-header .ql-picker-label::before,
.ql-snow .ql-picker.ql-header .ql-picker-item::before {
  content: "文本";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="1"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="1"]::before {
  content: "title1";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="2"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="2"]::before {
  content: "title2";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="3"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="3"]::before {
  content: "title3";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="4"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="4"]::before {
  content: "title4";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="5"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="5"]::before {
  content: "title5";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="6"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="6"]::before {
  content: "title6";
}

.ql-snow .ql-picker.ql-font .ql-picker-label::before,
.ql-snow .ql-picker.ql-font .ql-picker-item::before {
  content: "";
}
.ql-snow .ql-picker.ql-font .ql-picker-label[data-value="serif"]::before,
.ql-snow .ql-picker.ql-font .ql-picker-item[data-value="serif"]::before {
  content: "";
}
.ql-snow .ql-picker.ql-font .ql-picker-label[data-value="monospace"]::before,
.ql-snow .ql-picker.ql-font .ql-picker-item[data-value="monospace"]::before {
  content: "";
}
</style>
