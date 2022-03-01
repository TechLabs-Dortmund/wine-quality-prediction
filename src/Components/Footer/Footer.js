import React from "react";
import {
Box,
Container,
Row,
Column,
FooterLink,
Heading,
} from "./FooterStyles";

const Footer = () => {
return (
	<Box>
	<h1 style={{ color: "#ffff",
				textAlign: "center",
				marginTop: "-50px" }}>
		Vino Chance 🍷 Dein perfekter Wein
	</h1>
	<Container>
		<Row>
		<Column>
			<Heading>Über uns</Heading>
			<FooterLink href="#">Unsere Mission</FooterLink>
			<FooterLink href="#">Das Team</FooterLink>
		</Column>
		<Column>
			<Heading>Unser Angebot</Heading>
			<FooterLink href="#">Weine entdecken</FooterLink>
			<FooterLink href="#">Gerichte finden</FooterLink>
			<FooterLink href="#">Gut und Günstig</FooterLink>
			<FooterLink href="#">Über Wein</FooterLink>
		</Column>
		<Column>
			<Heading>Kontakt und Rechtliches</Heading>
			<FooterLink href="#">Kontakt</FooterLink>
			<FooterLink href="#">AGB</FooterLink>
			<FooterLink href="#">Impressum</FooterLink>
		</Column>
		<Column>
			<Heading>Social Media</Heading>
			<FooterLink href="#">
			<i className="fab fa-facebook-f">
				<span style={{ marginLeft: "10px" }}>
				Facebook
				</span>
			</i>
			</FooterLink>
			<FooterLink href="#">
			<i className="fab fa-instagram">
				<span style={{ marginLeft: "10px" }}>
				Instagram
				</span>
			</i>
			</FooterLink>
			<FooterLink href="#">
			<i className="fab fa-twitter">
				<span style={{ marginLeft: "10px" }}>
				Twitter
				</span>
			</i>
			</FooterLink>
			<FooterLink href="#">
			<i className="fab fa-youtube">
				<span style={{ marginLeft: "10px" }}>
				Youtube
				</span>
			</i>
			</FooterLink>
		</Column>
		</Row>
	</Container>
	</Box>
);
};
export default Footer;
