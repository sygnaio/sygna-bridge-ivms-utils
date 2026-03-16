# Sygna Bridge IVMS Util For Golang

## Installation
```
go get github.com/sygnaio/sygna-bridge-ivms-utils/golang
```

## Example
```go
package main

import (
	"encoding/json"
	"fmt"

	ivms101 "github.com/sygnaio/sygna-bridge-ivms-utils/golang/src/ivms2023"
)

type Ivms2023Payload struct {
	Originator      *ivms101.Originator      `json:"Originator,omitempty"`
	OriginatingVasp *ivms101.OriginatingVASP `json:"OriginatingVASP,omitempty"`
	Beneficiary     *ivms101.Beneficiary     `json:"Beneficiary,omitempty"`
}

func main() {
	// Originator
	// originator name id
	orgNameID := ivms101.NewNaturalPersonNameId()
	orgNameID.SetPrimaryIdentifier("Wu")
	orgNameID.SetSecondaryIdentifier("Xinli")
	orgNameID.SetNaturalPersonNameIdentifierType(string(ivms101.NATURALPERSONNAMETYPECODE_LEGL))

	// another name id for originator
	orgNameIDLocal := ivms101.NewLocalNaturalPersonNameId()
	orgNameIDLocal.SetPrimaryIdentifier("吳")
	orgNameIDLocal.SetSecondaryIdentifier("信利")
	orgNameIDLocal.SetNameIdentifierType(string(ivms101.NATURALPERSONNAMETYPECODE_LEGL))

	// assign two name id to originator name
	orgPersonName := ivms101.NewNaturalPersonName()
	orgPersonName.SetNameIdentifier([]ivms101.NaturalPersonNameId{*orgNameID})
	orgPersonName.SetLocalNameIdentifier([]ivms101.LocalNaturalPersonNameId{*orgNameIDLocal})

	// originator national id and data
	orgPersonNationalID := ivms101.NewNationalIdentification()
	orgPersonNationalID.SetNationalIdentifier("446005")
	orgPersonNationalID.SetNationalIdentifierType(string(ivms101.NATIONALIDENTIFIERTYPECODE_RAID))
	orgPersonNationalID.SetRegistrationAuthority("RA000553")

	// add geographic address info
	orgPersonAddress := ivms101.NewAddress()
	orgPersonAddress.SetAddressType(string(ivms101.GEOG))
	orgPersonAddress.SetStreetName("Potential Street")
	orgPersonAddress.SetBuildingNumber("24")
	orgPersonAddress.SetBuildingName("Weathering Views")
	orgPersonAddress.SetPostCode("91765")
	orgPersonAddress.SetTownName("Walnut")
	orgPersonAddress.SetCountrySubDivision("California")
	orgPersonAddress.SetCountry("US")

	// assign name, national id, country to originator natural person
	originatingNaturalPerson := ivms101.NewNaturalPerson()
	originatingNaturalPerson.SetName(*orgPersonName)
	originatingNaturalPerson.SetNationalIdentification(*orgPersonNationalID)
	originatingNaturalPerson.SetCountryOfResidence("TZ")
	originatingNaturalPerson.SetGeographicAddress([]ivms101.Address{*orgPersonAddress})

	// assign originator to person object
	originatingPerson := ivms101.NewPerson()
	originatingPerson.SetNaturalPerson(*originatingNaturalPerson)
	originatingPerson.SetAccountNumber([]string{"1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"})

	// assign originator person to originator object
	originator := ivms101.NewOriginator([]ivms101.Person{*originatingPerson})

	// construct originating vasp
	// name id for originating vasp
	origVaspNameID := ivms101.NewLegalPersonNameId()
	origVaspNameID.SetLegalPersonName("VASP A")
	origVaspNameID.SetLegalPersonNameIdentifierType(string(ivms101.LEGALPERSONNAMETYPECODE_LEGL))

	// name for originating vasp
	origVaspName := ivms101.NewLegalPersonName([]ivms101.LegalPersonNameId{*origVaspNameID})
	origVaspName.SetNameIdentifier([]ivms101.LegalPersonNameId{*origVaspNameID})

	// national ID for originating vasp
	origVaspNationalID := ivms101.NewNationalIdentification()
	origVaspNationalID.SetNationalIdentifier("3M5E1GQKGL17HI8CPN20")
	origVaspNationalID.SetNationalIdentifierType(string(ivms101.NATIONALIDENTIFIERTYPECODE_LEIX))

	// legal person for originating vasp
	origVaspLegalPerson := ivms101.NewLegalPerson(*origVaspName)
	origVaspLegalPerson.SetName(*origVaspName)
	origVaspLegalPerson.SetNationalIdentification(*origVaspNationalID)

	// person for originating vasp
	origVaspPerson := ivms101.NewPerson()
	origVaspPerson.SetLegalPerson(*origVaspLegalPerson)

	origVasp := ivms101.NewOriginatingVASP()
	origVasp.SetOriginatingVASP(*origVaspPerson)

	// Beneficiary
	// beneficiary 1 name id
	bene1NameID := ivms101.NewLegalPersonNameId()
	bene1NameID.SetLegalPersonName("ABC Limited")
	bene1NameID.SetLegalPersonNameIdentifierType(string(ivms101.LEGALPERSONNAMETYPECODE_LEGL))

	// assign beneficiary 1 name with id
	bene1PersonName := ivms101.NewLegalPersonName([]ivms101.LegalPersonNameId{*bene1NameID})
	bene1PersonName.SetNameIdentifier([]ivms101.LegalPersonNameId{*bene1NameID})

	// beneficiary 1 is a legal person
	beneficiary1LegalPerson := ivms101.NewLegalPerson(*bene1PersonName)
	beneficiary1LegalPerson.SetName(*bene1PersonName)

	// assign beneficiary 1 to person object
	beneficiary1Person := ivms101.NewPerson()
	beneficiary1Person.SetLegalPerson(*beneficiary1LegalPerson)

	// beneficiary 2 name id
	bene2NameID := ivms101.NewLegalPersonNameId()
	bene2NameID.SetLegalPersonName("CBA Trading")
	bene2NameID.SetLegalPersonNameIdentifierType(string(ivms101.LEGALPERSONNAMETYPECODE_TRAD))

	// assign beneficiary 2 name with id
	bene2PersonName := ivms101.NewLegalPersonName([]ivms101.LegalPersonNameId{*bene2NameID})
	bene2PersonName.SetNameIdentifier([]ivms101.LegalPersonNameId{*bene2NameID})

	// beneficiary 2 is a legal person
	beneficiary2LegalPerson := ivms101.NewLegalPerson(*bene2PersonName)
	beneficiary2LegalPerson.SetName(*bene2PersonName)

	// assign beneficiary 2 to person object
	beneficiary2Person := ivms101.NewPerson()
	beneficiary2Person.SetLegalPerson(*beneficiary2LegalPerson)

	// assign both persons to beneficiary object
	beneficiary := ivms101.NewBeneficiary([]ivms101.Person{*beneficiary1Person, *beneficiary2Person})

	// assign originator and beneficiary data to identity payload
	privateInfo := Ivms2023Payload{
		Originator:      originator,
		OriginatingVasp: origVasp,
		Beneficiary:     beneficiary,
	}

	// to json
	jsonb, _ := json.MarshalIndent(privateInfo, "", "  ")
	fmt.Print(string(jsonb))

	// from json
	var decoded Ivms2023Payload
	_ = json.Unmarshal(jsonb, &decoded)
	jsonb2, _ := json.MarshalIndent(decoded, "", "  ")
	fmt.Println("\n\n" + string(jsonb2))
}
```