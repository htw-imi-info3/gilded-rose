
```mermaid
classDiagram
    AgingItem <|-- NormalItem
    NormalItem <|-- ConjuredItem
    AgingItem <|-- BackstagePass
    AgingItem <|-- AgedBrie
  
    class AgingItem{
      update()
      _cap_quality()
      _quality_change()
      _update_hook()
    }
    class NormalItem{
      _quality_change()
    }
     class AgedBrie{
      _quality_change()
    }
    class BackstagePass{
      _quality_change()
      _update_hook()
    }
    class ConjuredItem{
      _quality_change()
    }
    class Sulfuras{
        update()
    }
    
    
    
```