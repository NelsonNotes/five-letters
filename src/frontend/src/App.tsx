import React, { useEffect } from 'react'
import { BrowserRouter, Routes } from 'react-router-dom'

import { useAppDispatch } from './hooks/app'
import { useSelector } from 'react-redux'
import { sessionOperations } from './store/session/operations'
import { selectSession } from './store/session/selectors'
import { Route, redirect } from 'react-router-dom'
import { sessionClear } from './store/session/utils'
import { GamePage } from './components/game/GamePage'
import { LoginPage } from './components/login/LoginPage'

export const App: React.FC = () => {
	const dispatch = useAppDispatch()

	const session = useSelector(selectSession)

	useEffect(() => {
		redirect('/')
	}, [session])

	return (
		<BrowserRouter>
			{session.data ? (
				<Routes>
					<Route path='*' element={<GamePage />} />
				</Routes>
			) : (
				<Routes>
					<Route path='*' element={<LoginPage />} />
				</Routes>
			)}
		</BrowserRouter>
	)
}
