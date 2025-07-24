<?php

class HtmlTag {
  protected static $allowedAttributes = ['id', 'class', 'title', 'style'];

  protected $tagName = '';

  protected $attributes = [];

  protected $children = [];

  protected $content = '';

  public function __construct($tagName, $attributes = [],
      $content = '') {
    $this->tagName = $tagName;
    if (!empty($attributes)) {
      foreach ($attributes as $name => $value) {
        $this->addAttribute($name, $value);
      }
    }
    $this->content = $content;
  }

  public function addAttribute($name, $value) {
    if (in_array($name, self::$allowedAttributes)) {
      $this->attributes[$name] = $value;
    }
  }

  public function addChild($child) {
    $this->children[] = $child;
  }

  public function __toString() {
    $result = sprintf('<%s', htmlspecialchars($this->tagName));
    foreach ($this->attributes as $name => $value) {
      $result .= sprintf(
        ' %s="%s"',
        htmlspecialchars($name),
        htmlspecialchars($value)
      );
    }
    if (!empty($this->content)) {
      $result .= ">\n";
      $result .= $this->content;
      $result .= sprintf("</%s>\n", htmlspecialchars($this->tagName));
    } elseif (!empty($this->children)) {
      $result .= ">\n";
      foreach ($this->children as $child) {
        $result .= $child->__toString();
      }
      $result .= sprintf("</%s>\n", htmlspecialchars($this->tagName));
    } else {
      $result .= " />\n";
    }
    return $result;
  }
}

class Html extends HtmlTag {
  protected $head = NULL;

  protected $body = NULL;

  public function __construct($head, $body) {
    parent::__construct('html');
    $this->head = $head;
    $this->body = $body;
  }

  public function __toString() {
    $this->content = $this->head->__toString();
    $this->content .= $this->body->__toString();
    return parent::__toString();
  }
}

class Head extends HtmlTag {
  protected $title = NULL;

  protected $metaTags = [];

  public function __construct($title, $metaTags = []) {
    parent::__construct('head');
    $this->title = $title;
    $this->metaTags = $metaTags;
  }

  public function addMetaTag($metaTag) {
    $this->metaTags[] = $metaTag;
  }

  public function __toString() {
    $this->content = $this->title->__toString();
    foreach ($this->metaTags as $metaTag) {
      $this->content .= $metaTag->__toString();
    }
    return parent::__toString();
  }
}

class Title extends HtmlTag {
  public function __construct($content) {
    parent::__construct('title', [], $content);
  }
}

class Meta extends HtmlTag {
  public function __construct($attributes = []) {
    parent::__construct('meta');
    self::$allowedAttributes = ['name', 'http-equiv', 'content', 'charset'];
    foreach ($attributes as $name => $value) {
      $this->addAttribute($name, $value);
    }
  }
}

class Body extends HtmlTag {
  public function __construct() {
    parent::__construct('body');
  }
}

class Hn extends HtmlTag {
  public function __construct($level, $content) {
    parent::__construct('h'.$level, [], $content);
  }
}

class P extends HtmlTag {
  public function __construct($attributes, $content) {
    parent::__construct('p', $attributes, $content);
    self::$allowedAttributes = ['id', 'class', 'title', 'style', 'align'];
  }
}

$head = new Head(new Title('HTML-Ausgabe durch PHP-Klassen'));
$head->addMetaTag(new Meta(['http-equiv' => 'Content-type', 'content' => 'text/html; charset=utf-8']));
$head->addMetaTag(new Meta(['name' => 'description', 'content' => 'Von PHP generiertes HTML']));
$body = new Body();
$body->addChild(new Hn(1, 'HTML-Ausgabe'));
$body->addChild(new P([], 'Dieses Dokument wird mithilfe von PHP-Klassen ausgegeben.'));
$body->addChild(new Hn(2, 'HtmlTag'));
$body->addChild(new P([], 'Dies ist die Elternklasse aller HTML-Tags.'));
$body->addChild(new Hn(2, 'Html, Head, Body, P etc.'));
$body->addChild(new P([], 'Diese Klassen sind von HtmlTag oder voneinander abgeleitet.'));
$body->addChild(new P(['align' => 'right'], 'Aus: "IT-Handbuch für Fachinformatiker*innen'));
$html = new Html($head, $body);
echo $html;
