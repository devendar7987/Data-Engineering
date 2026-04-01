# 🧠 XSD Concept (XML Schema Definition)

## 📌 What is XSD?

XSD (XML Schema Definition) defines the structure of an XML document.

It specifies:
- Elements and attributes
- Data types (int, string, etc.)
- Mandatory and optional fields
- Parent-child relationships

---

## 🧱 Example XSD

```xml
<xs:element name="product">
   <xs:complexType>
      <xs:sequence>
         <xs:element name="id" type="xs:int"/>
         <xs:element name="name" type="xs:string"/>
         <xs:element name="price" type="xs:int"/>
      </xs:sequence>
   </xs:complexType>
</xs:element>