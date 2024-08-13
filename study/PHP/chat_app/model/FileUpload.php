<?php
class FileUpload {
    private $allowedTypes = ['image/jpeg', 'image/png', 'video/mp4', 'audio/mp3'];
    private $allowedExt = ['jpg', 'jpeg', 'png', 'mp4', 'mp3'];
    private $maxFileSize = 10 * 1024 * 1024; // 10MB

    public function upload($file) {
        if ($this->validateFile($file)) {
            $uploadDir = "../uploads/";
            $ext = strtolower(pathinfo($file["name"], PATHINFO_EXTENSION));
            $newFileName = time() . rand(1000, 9999) . "." . $ext;
            $uploadFile = $uploadDir . $newFileName;

            if (move_uploaded_file($file["tmp_name"], $uploadFile)) {
                return 'uploads/' . $newFileName; // 返回相对于项目根目录的路径
            } else {
                throw new Exception("Failed to move uploaded file.");
            }
        }
    }

    private function validateFile($file) {
        $fileType = $file["type"];
        $fileSize = $file["size"];
        $ext = strtolower(pathinfo($file["name"], PATHINFO_EXTENSION));

        if (!in_array($fileType, $this->allowedTypes) || !in_array($ext, $this->allowedExt)) {
            throw new Exception("Invalid file type.");
        }

        if ($fileSize > $this->maxFileSize) {
            throw new Exception("File size is too large.");
        }

        return true;
    }
}
?>
